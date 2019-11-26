from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


classrooms = []
subjects = [
    "Acctg",
    "Aero",
    "AFS",
    "Ag_Ed",
    "Agri",
    "AgTM",
    "AIS",
    "AMT",
    "Am_St",
    "A_S",
    "Anth",
    "Arch",
    "Asia",
    "Astr",
    "Ath_T",
    "B_A",
    "B_Law",
    "B_E",
    "Biol",
    "BSysE",
    "CAS",
    "C_E",
    "CES",
    "Ch_E",
    "Chem",
    "Chin",
    "Com",
    "COMHL",
    "ComJo",
    "ComSo",
    "ComSr",
    "CON_E",
    "CoPsy",
    "Cpt_S",
    "Crm_J",
    "CropS",
    "CSSTE",
    "Cst_M",
    "DTC",
    "E_E",
    "E_M",
    "E_Mic",
    "EconS",
    "Ed_Ad",
    "MTHSC",
    "EdPsy",
    "EdRes",
    "Engl",
    "Engr",
    "Entom",
    "Entrp",
    "Fin",
    "F_A",
    "For_L",
    "Fren",
    "FS",
    "Ger",
    "GAH",
    "H_D",
    "HBM",
    "Hist",
    "U_H",
    "Hort",
    "Hum",
    "I_Bus",
    "I_D",
    "Univ",
    "ISE",
    "Japn",
    "Kines",
    "LLT",
    "L_A",
    "Math",
    "Mat_S",
    "MBioS",
    "M_E",
    "MGMT",
    "MgtOp",
    "Mil_S",
    "MIS",
    "MIT",
    "Mktg",
    "MPS",
    "MSE",
    "Mus",
    "Neuro",
    "PEACT",
    "PHRDS",
    "Phil",
    "Phys",
    "Pl_P",
    "Pol_S",
    "PrvSc",
    "Psych",
    "Sci",
    "SDC",
    "SHS",
    "Soc",
    "SOE",
    "SoilS",
    "Span",
    "Sp_Ed",
    "SpMgt",
    "Stat",
    "T_%5E_L",
    "Univs",
    "W_St",
    "WRIT",
]

def get_all_html_content_from_url(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    Taken from: https://realpython.com/python-web-scraping-practical-introduction/
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response appears to be HTML, false otherwise
    Taken from: https://realpython.com/python-web-scraping-practical-introduction/
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    """
    Logs errors by simply printing them 
    Taken from: https://realpython.com/python-web-scraping-practical-introduction/
    """
    print(e)

def get_all_classroom_data(url):
    """
    Collects all of the classroom data.
    """
    for prefix in subjects:
        url = url + "/" + prefix
        html_data = get_all_html_content_from_url(url)
        extract_data_from_html(html_data)

def extract_data_from_html(html_data):
    """
    Extract the necessary data from the html.
    """
    html = BeautifulSoup(html_data, 'html.parser')
