import pdfminer
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import nltk
import re
from nltk.corpus import stopwords


class Resume(object):

    def __init__(self, file):
        self.file = file
        
  
  
  
    def parse_file(self):
        with open(self.file, 'rb') as fh:
            # iterate over all pages of PDF document
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            # creating a resoure manager
                resource_manager = PDFResourceManager()

            # create a file handle
                fake_file_handle = io.StringIO()

            # creating a text converter object
                converter = TextConverter(
                                resource_manager,
                                fake_file_handle,
                                codec='utf-8',
                                laparams=LAParams()
                        )

            # creating a page interpreter
                page_interpreter = PDFPageInterpreter(
                                resource_manager,
                                converter
                            )

            # process current page
                page_interpreter.process_page(page)

            # extract text
                text = fake_file_handle.getvalue()

                stop = stopwords.words('english')
                res_clean = text.replace("-", " ")
                res_clean = res_clean.replace(",", "")
                res_clean = re.sub("[\n]", " ",res_clean)
                res_clean = re.sub("[.!?/\()-,_:]", "",res_clean)
                #es_clean = res_clean.lower()
                res_clean = " ".join([word for word in res_clean.split(" ") if word not in stop])
                subs = re.sub("[\d+][+-]", "",res_clean)
                subs = re.sub("[’']", "",res_clean)
                
                return res_clean

                # close open handles
                # converter.close()
                # fake_file_handle.close()





      