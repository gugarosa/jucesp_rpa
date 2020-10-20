# Waiting time
WAITING_TIME = 5

# Advanced search's URL
SEARCH_URL = 'https://www.jucesponline.sp.gov.br/BuscaAvancada.aspx'

# Form's x-paths and values
FORM = {
    'city': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtMunicipio"]', 'araraquara'),
    'start_date': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtDataAberturaInicio"]', '01/09/2020'),
    'end_date': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtDataAberturaFim"]', '30/09/2020')
}

# Submit button x-path
SUBMIT = '//*[@id="ctl00_cphContent_frmBuscaAvancada_btPesquisar"]'

# Capctha x-paths
CAPTCHA = '/html/body/div[3]/form/div[3]/div[4]/div[2]/div/div/table/tbody/tr[1]/td/div/div[1]/img'
CAPTCHA_INPUT = '/html/body/div[3]/form/div[3]/div[4]/div[2]/div/div/table/tbody/tr[1]/td/div/div[2]/label/input'
CAPTCHA_SUBMIT = '//*[@id="ctl00_cphContent_gdvResultadoBusca_btEntrar"]'

# Results table and next page button x-paths
RESULTS_TABLE = '//*[@id="ctl00_cphContent_gdvResultadoBusca_gdvContent"]'
RESULTS_NEXT_PAGE = '//*[@id="ctl00_cphContent_gdvResultadoBusca_pgrGridView_btrNext_lbtText"]'
RESULTS_NEXT_PAGE_SCRIPT = "__doPostBack('ctl00$cphContent$gdvResultadoBusca$pgrGridView$btrNext$lbtText','')"
