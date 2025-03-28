import os
from django.conf import settings
from django.template.loader import render_to_string, get_template
from django.http import FileResponse
import asyncio
from playwright.async_api import async_playwright, expect

from apps.CV.models import Block


async def html_to_pdf(html_content, output_path, css):

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # await expect(page.get_by_test_id('left-side')).toHaveCSS(
        #     "background-color",
        #     css['left-side']['color']
        # )
        # await expect(page.get_by_test_id('right-side')).toHaveCSS(
        #     "background-color",
        #     css['right-side']['color']
        # )
        await page.locator('body').evaluate("element => element.style.display = 'flex'")
        # await page.locator("#right-side").evaluate("element => element.style.display = 'flex'")
        await page.set_content(html_content)
        await page.pdf(path=output_path)
        await browser.close()

class Generator:


    def generatedownloaderResponse(self, cv):
        """
        Parameters
        ----------
        content: str content to write in the pdf file
        output: str name of the file to create
        """
        filename = 'CV_' + cv.name + '.pdf'

        Cvblocks = Block.manager.getByCv(cv)
        # # Open file to write
        content = self.getTemplate(cv, Cvblocks)

        if not os.path.isdir("./files"):
            os.mkdir("./files")

        asyncio.run(html_to_pdf(content, './files/' + filename, {'left-side': {'color': cv.primaryColor}, 'right-side': {'color': cv.secondaryColor}}))

        response = FileResponse(open('./files/' + filename, 'rb'), content_type="application/pdf")
        response['Content-Disposition'] = 'attachment; filename="CV_' + cv.name + '.pdf"'

        return response

    def getTemplate(self, cv, blocks=None, lines=None, details=None):
        template = "templatesFilesHTML/" + cv.template
        return render_to_string(template, {"cv": cv, 'blocks': blocks, 'lines':lines, 'details': details})