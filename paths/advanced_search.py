# Waiting time
WAITING_TIME = 5

# Advanced search URL
URL = 'https://www.jucesponline.sp.gov.br/BuscaAvancada.aspx'

# Form x-paths
FORM = {
    # 'razao_social': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtRazaoSocial"]', ''),
    # 'tipo_empresa:': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_ddlTipoEmpresa"]', ''),
    # 'objeto': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtObjeto"]', ''),
    # 'capital_min': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtCapitalMin"]', ''),
    # 'capital_max': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtCapitalMax"]', ''),
    'data_abertura_inicio': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtDataAberturaInicio"]', '01/09/2020'),
    'data_abertura_fim': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtDataAberturaFim"]', '30/09/2020'),
    # 'data_dissolucao_inicio': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtDataDissolucaoInicio"]', ''),
    # 'data_dissolucao_fim': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtDataDissolucaoFim"]', ''),
    # 'empresa_ativa': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_chkAtivas"]', ''),
    'municipio': ('//*[@id="ctl00_cphContent_frmBuscaAvancada_txtMunicipio"]', 'araraquara')
}
FORM_SUBMIT = '//*[@id="ctl00_cphContent_frmBuscaAvancada_btPesquisar"]'

# Captcha x-paths
CAPTCHA = '/html/body/div[3]/form/div[3]/div[4]/div[2]/div/div/table/tbody/tr[1]/td/div/div[1]/img'
CAPTCHA_INPUT = '/html/body/div[3]/form/div[3]/div[4]/div[2]/div/div/table/tbody/tr[1]/td/div/div[2]/label/input'
CAPTCHA_SUBMIT = '//*[@id="ctl00_cphContent_gdvResultadoBusca_btEntrar"]'

# Results and next page button x-paths
RESULTS = '//*[@id="ctl00_cphContent_gdvResultadoBusca_gdvContent"]'
RESULTS_NEXT_PAGE = '//*[@id="ctl00_cphContent_gdvResultadoBusca_pgrGridView_btrNext_lbtText"]'
RESULTS_NEXT_PAGE_SCRIPT = "__doPostBack('ctl00$cphContent$gdvResultadoBusca$pgrGridView$btrNext$lbtText','')"
