

# CONVERTER DATAFRAMES DO PANDAS EM UMA TABELA INTERATIVA COM PAGINAÇÃO E PODEREMOS REALIZAR CLASSIFICAÇÃO


import pandas as pd

import webbrowser

from io import StringIO

#  O MODULO WEBBROWSER ABRE AUTOMATICAMENTE A TABELA HTML RESULTANTE EM UMA NOVA GUIA NO NAVEGADOR PADRÃO

# AGORA IREMOS CRIAR UMA FUNÇÃO QUE ACEITE O DATAFRAME COMO ARGUMENTO E RETORNE O CONTEUDO HTML PARA ISSO:

def generate_html(dataframe: pd.DataFrame):
    # obtém o HTML da tabela no dataframe
    table_html = dataframe.to_html(table_id="table")
    # constrói o HTML completo com tabelas de dados jQuery
    # Você pode desativar a paginação ou ativar a rolagem nas linhas 20 e 21 respectivamente
    html = f"""
    <html>
    <header>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
    </header>
    <body>
    {table_html}
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#table').DataTable({{
                // paging: false,    
                // scrollY: 400,
            }});
        }});
    </script>
    </body>
    </html>
    """
    # RETORNA O HTML
    return html


# AQUI VERIFICAMOS SE O SCRIPT ESTA NO MODULO PRINCIPAL
# LEMOS O ARQUIVO CSV E SELECIONAMOS OS PRIMEIROS 1000 DADOS
# E CHAMAMOS A FUNÇÃO GENERATE_HTML
# E POR FIM O ARQUIVO HTML E ABERTO NO NAVEGADOR
# PEGUEI ESSE ARQUIVO CSV NO GITHUB E MUDEI O NOME NA MINHA PASTE, SEGUE ABAIXO O LINK DO ARQUIVO:
# https://github.com/x4nth055/pythoncode-tutorials/blob/master/general/dataframe-to-html/Churn_Modelling.csv

if __name__ == "__main__":
    # read the dataframe dataset
    df = pd.read_csv('C:\\Users\\Usuario\\Desktop\\PROJETOS PYTHON\\dados.csv')
    # take only first 1000, otherwise it'll generate a large html file
    df = df.iloc[:1000]
    # generate the HTML from the dataframe
    html = generate_html(df)
    # write the HTML content to an HTML file
    with open("index.html", "w") as f:
        f.write(html)
    # open the new HTML file with the default browser
    webbrowser.open("index.html")


