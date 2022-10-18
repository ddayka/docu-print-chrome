# pdf-print-chrome
Automatically Print PDF Documents via Google Chrome

**Requirements:** <br>
This Code uses Selenium and Google Chrome (meaning you will need correct ChromeDriver for your version of Chrome) <br>
Download ChromeDriver Here: https://chromedriver.chromium.org/downloads <br>

**Inputs:** <br>
_Required:_ <br>
File of Document/Picture you want to print <br>

_Optiona:_ <br>
Printer (str): name of printer you want to use (default printer selected by default) <br>
copies (int): number of copies printer (1 selected by default) <br>
color (Bool): Color vs Black and White (Color True Selected by default) <br>
paper_size (str): Choose available letter sizes ('letter' by default) <br>
page_per_sheet (int): # pages per sheet of paper (1 by default) <br>
scale (str): can be 'Fit to Paper' or 'Fit to Printable Area' or 'Custom' (if custom see below) ('default' by default) <br>
custom_scale (int): if scale = 'custom' then custom scale size will be this % of size (100 by default) <br>
two_sided (Bool): print on both side of paper (False by default) <br>
