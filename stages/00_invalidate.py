import asyncio, re, os
from urllib.parse import urljoin
from pyppeteer import launch

async def main():
    base_url = 'https://cwtung.kmu.edu.tw/skinsensdb/download'
    
    browser = await launch()
    page = await browser.newPage()
    await page.goto(base_url, {'waitUntil': 'networkidle2'})
    html_content = await page.content()
    
    # Extract TSV links using regular expression
    links = re.findall(r'href="([^"]+\.tsv)"', html_content)
    full_urls = [urljoin(base_url, link) for link in links]
    
    # write links to file cache/00_invalidate/links.txt
    os.makedirs('cache/00_invalidate', exist_ok=True)
    with open('cache/00_invalidate/links.txt', 'w') as file:
        for link in full_urls:
            file.write(f"{link}\n")
    
asyncio.get_event_loop().run_until_complete(main())