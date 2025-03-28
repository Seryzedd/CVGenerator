from django.contrib import messages
from django.db import IntegrityError
from django.middleware import http
from django.shortcuts import render, redirect
from apps.CV.forms.CVForm import CvForm
from apps.CV.models import Line
from apps.CV.models.CV import CV
from apps.CV.models.Block import Block
from django.http import HttpResponse
from xhtml2pdf import pisa
from apps.CV.fileGenerator.generator import Generator
from apps.CV.models.line import LineManager


def CV_id_view(request):
    if not request.user.is_authenticated:
        messages.info(request, "You need to login to create CV.")
        return redirect('login')
    form = CvForm(request.POST or None)

    if form.is_valid():
        try:
            cleaned_data = form.clean()

            new_cv = CV()
            new_cv.update(
                {
                    'name': cleaned_data['name'],
                    'description': cleaned_data['description'],
                    'template': cleaned_data['template'],
                    'primaryColor': cleaned_data['primaryColor'],
                    'secondaryColor': cleaned_data['secondaryColor']
                },
                request.user
            )

            messages.success(request, "CV créé !")

            messages.info(request, "Vous pouvez completer la configuration du CV.")

            return redirect('home')
        except IntegrityError:
            messages.error(request, 'Erreur lors de la génération du CV.')
        except Exception as e:
            messages.error(request, f"Une erreur est survenue : {e}")

    return render(request, 'CVNew/index.html', {'form': form})


def CVManageExistingCV(request, name):
    cv = CV.object.getByName(name)
    form = CvForm()
    form.setData(cv)

    Cvblocks = Block.manager.getByCv(cv)

    blocksIds = {block.id: block for block in Cvblocks}

    lines = LineManager().getByBlocks(blocksIds)

    post = request.POST
    if post:

        try:
            cv = cv.update(post)
            blocklist = {}
            lineParameters = {}
            for paramName, param in dict(post).items():
                splittedParam = paramName.split('-')
                last = None
                if len(splittedParam) > 1:
                    last = splittedParam[len(splittedParam) - 1]

                if 'block' in splittedParam and 'line' not in splittedParam:
                    blocknumber = int(paramName[-1:]) - 1

                    if blocknumber not in blocklist.keys():
                        blocklist[blocknumber] = {}
                    if 'block-name-' in paramName:
                        blocklist[blocknumber]['name'] = param[0]
                    if 'block-placement-' in paramName:
                        blocklist[blocknumber]['placement'] = param[0]
                    if paramName[:8] == 'block-id':
                        blocklist[blocknumber]['id'] = int(splittedParam[2])

                if 'line' in paramName:
                    if last not in lineParameters.keys():
                        lineParameters.update({last:{}})
                    line = Line()
                    if 'new' not in paramName:
                        for lineentity in lines:
                            if lineentity.id == int(last):
                                line = lineentity
                                break


                    if 'title' in paramName:
                        lineParameters.get(last).update({'title': post[paramName]})
                    if 'startAt' in paramName:
                        lineParameters.get(last).update({'startAt': post[paramName]})
                    if 'endAt' in paramName:
                        lineParameters.get(last).update({'endAt': post[paramName]})

                    lineParameters.get(last).update({'block_id': splittedParam[1]})
                    lineParameters.get(last).update({'entity': line})

                    # lineParameters.update({last: lineparams})

            for blockParameters in range(len(blocklist)):
                block = Block()
                if "id" in blocklist[blockParameters].keys():
                    for cvblock in Cvblocks:
                        if cvblock.id == blocklist[blockParameters]['id']:
                            block = cvblock

                blocklist[blockParameters]['cv'] = cv
                block.update(blocklist[blockParameters])

            print(post)
            for param in lineParameters.items():
                entity = param[1]['entity']
                print(param[1])
                param[1].update({'block': blocksIds[int(param[1]['block_id'])]})
                entity.update(param[1])


            messages.success(request, "CV Modifié !")

            return redirect('cvTemplateRender', id=cv.id)

        except IntegrityError:
            messages.error(request, 'Erreur lors de la mise a jour du CV.')
        # except Exception as e:
        #     messages.error(request, f"Une erreur est survenue : {e}")

    Cvblocks = Block.manager.getByCv(cv)
    blocksIds = {block.id: block for block in Cvblocks}
    lines = LineManager().getByBlocks(blocksIds)
    lineskeys = [line.block.id for line in lines]
    form.setData(cv)


    return render(request, 'CVUpdate/CvUpdater.html', {'form': form, 'cv': cv, 'cvblocks': Cvblocks, 'lines': lines, 'linesKeys': lineskeys})


def CVTemplateView(request, id):
    cv = CV.object.getById(id)

    html = None
    if cv:
        blocks = Block.manager.getByCv(cv)
        form = CvForm()
        form.setData(cv)
        blocksIds = {block.id: block for block in blocks}
        lines = LineManager().getByBlocks(blocksIds)
        lineskeys = [line.block.id for line in lines]

        generator = Generator()
        templateLoad = generator.getTemplate(cv, blocks, lines, None, request.user)
        # html = templateLoad.render({'cv': cv}, request)

    return render(request, 'CvTemplaterender/view.html', {'cv': cv, 'html': templateLoad, 'form': form})

def generatePDF(request, id):
    cv = CV.object.getById(id)

    if cv:
        generator = Generator()
        # Open file to write
        response = generator.generatedownloaderResponse(cv)

        return response


