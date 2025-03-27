from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from apps.CV.forms.CVForm import CvForm
from apps.CV.models.CV import CV
from apps.CV.models.Block import Block
from django.template import loader


def CV_id_view(request):
    if not request.user.is_authenticated:
        messages.info(request, "You need to login to create CV.")
        return redirect('login')
    form = CvForm(request.POST or None)
    if form.is_valid():
        try:
            cleaned_data = form.clean()

            new_cv = CV()
            new_cv.object.createNew(
                name=cleaned_data['name'],
                description=cleaned_data['description'],
                template=cleaned_data['template'],
                primaryColor=cleaned_data['primaryColor'],
                secondaryColor=cleaned_data['secondaryColor'],
                user=request.user
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
    post = request.POST
    if post:
        try:
            cv = cv.update(post)
            blocklist = {}
            for paramName, param in dict(post).items():

                if paramName[:5] == 'block':
                    i = 0
                    blocknumber = int(paramName[-1:]) -1

                    if blocknumber not in blocklist.keys():
                        blocklist[blocknumber] = {}
                    if 'block-name-' in paramName:
                        blocklist[blocknumber]['name'] = param[0]
                    if 'block-placement-' in paramName:
                        blocklist[blocknumber]['placement'] = param[0]
                    if paramName[:8] == 'block-id':
                        blocklist[blocknumber]['id'] = param[0]

                    blocklist[blocknumber]['cv'] = cv


            for blockParameters in range(len(blocklist)):
                block = Block()
                if "id" in blocklist[blockParameters].keys():
                    for cvblock in Cvblocks:
                        if cvblock.id == blocklist[blockParameters]['cv']:
                            block = cvblock

                block.update(blocklist[blockParameters])

            messages.success(request, "CV Modifié !")

            return redirect('cvTemplateRender', id=cv.id)

        except IntegrityError:
            messages.error(request, 'Erreur lors de la mise a jour du CV.')
        except Exception as e:
            messages.error(request, f"Une erreur est survenue : {e}")

    Cvblocks = Block.manager.getByCv(cv)
    form.setData(cv)

    return render(request, 'CVUpdate/CvUpdater.html', {'form': form, 'cv': cv, 'cvblocks': Cvblocks})

def CVTemplateView(request, id):
    cv = CV.object.getById(id)

    form = CvForm()
    form.setData(cv)

    html = None
    if cv:
        template = "templatesFilesHTML/" + cv.template
        templateLoad = loader.get_template(template)
        # html = render(request, template, {'cv': cv})
        html = templateLoad.render({'cv': cv}, request)
        print(html)
    return render(request, 'CvTemplaterender/view.html', {'cv': cv, 'html': html, 'form': form})
