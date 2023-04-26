from var import *
from load_bq import *
from generate_data import *
from create_bq import *
from extract_bq import *

#Service account key file path

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../key.json"

create_bq()
filename = generate_data(500)  # 500 is count of records generated you can give number as you want
load_bq(filename)
extract_bq()
