# tx-land-grant-db-scraper
A web scraper to navigate to pdf file by file number in the [Texas LGO Land Grant Database](http://www.glo.texas.gov/history/archives/land-grants/index.cfm)

# How to use
The script is hosted at http://18.221.185.38, which will redirect you to a pdf file based on file number. It takes requests like `http://18.221.185.38/?[FILE_NO]`
For example, http://18.221.185.38/?106061 redirects to the pdf for file number 106061. Replacing the last six digits with any valid file number will redirect you to the pdf.

This could be used in an excel column with the links to each file, with a function generating urls based on the file number like:

`=CONCATENATE("http://18.221.185.38/?",A2)`

where A2 contains the file number for that row.

