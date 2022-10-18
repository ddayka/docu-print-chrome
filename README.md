# pdf-print-chrome
Automatically Print Document via Google Chrome

Requirements:
This Code uses Selenium and Google Chrome (meaning you will need correct ChromeDriver for your version of Chrome)
Download ChromeDriver Here: https://chromedriver.chromium.org/downloads

Inputs:
Required: 
File of Document/Picture you want to print

Optional: 
Printer (str): name of printer you want to use (default printer selected by default)
copies (int): number of copies printer (1 selected by default)
color (Bool): Color vs Black and White (Color True Selected by default)
paper_size (str): Choose available letter sizes ('letter' by default)
page_per_sheet (int): # pages per sheet of paper (1 by default)
scale (str): can be 'Fit to Paper' or 'Fit to Printable Area' or 'Custom' (if custom see below) ('default' by default)
custom_scale (int): if scale = 'custom' then custom scale size will be this % of size (100 by default)
two_sided (Bool): print on both side of paper (False by default)
