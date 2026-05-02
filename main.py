import json
import re
import os

def clean_text(text):
    """
    Limpa o texto para evitar erros de leitura no IRaMuTeQ.
    """
    if not text or text in ["[deleted]", "[removed]"]:
        return ""

    # Limpeza e padronização dos dados, removendo URLs, quebras de linha e tabulações, caracteres inválidos ou emojis, espaços em branco extras e pontuação desnecessária. Por fim, convertemos todo o texto para minúsculas.
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[\n\t\r]', ' ', text)
    text = re.sub(r'[^a-zA-ZÀ-ÿ0-9\s.,!?\'-]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.lower()

    return text

def extract_comments(comments_list, subreddit, thread_id):
    """
    Função recursiva para extrair comentários e suas respostas.
    """
    extracted = []
    for comment in comments_list:
        body = clean_text(comment.get('body', ''))
        
        if body:
            score = comment.get('score', 0)
            
            # Categorização do engajamento para criar variáveis no IRaMuTeQ
            if score >= 50:
                score_cat = "alto"
            elif score >= 10:
                score_cat = "medio"
            else:
                score_cat = "baixo"

            # Linha de comando/categorização obrigatória para o IRaMuTeQ (**** *var1 *var2)
            header = f"**** *subreddit_{subreddit.lower()} *thread_{thread_id} *engajamento_{score_cat}"
            extracted.append(f"{header}\n{body}\n")
        
        # Busca por respostas aninhadas e chama a função recursivamente
        if 'replies' in comment and isinstance(comment['replies'], list) and len(comment['replies']) > 0:
            extracted.extend(extract_comments(comment['replies'], subreddit, thread_id))
            
    return extracted

def process_directory(input_dir, output_filepath):
    """
    Lê todos os arquivos JSON de um diretório e compila um único arquivo .txt para o IRaMuTeQ.
    """
    if not os.path.exists(input_dir):
        print(f"Erro: O diretório '{input_dir}' não foi encontrado.")
        return

    all_texts_to_write = []
    arquivos_processados = 0

    # Itera sobre todos os arquivos na pasta
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            json_filepath = os.path.join(input_dir, filename)
            
            with open(json_filepath, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    print(f"Erro ao ler o arquivo {filename}. Ignorando.")
                    continue
            
            post_info = data.get('post', {})
            subreddit = post_info.get('subreddit', 'unknown')
            thread_id = post_info.get('id', 'unknown')
                        
            # Extrai o corpo do Post original
            post_body = clean_text(post_info.get('body', ''))
            if post_body:
                header_post = f"**** *subreddit_{subreddit.lower()} *thread_{thread_id} *tipo_post"
                all_texts_to_write.append(f"{header_post}\n{post_body}\n")
            
            # Extrai os comentários
            comments = data.get('comments', [])
            all_texts_to_write.extend(extract_comments(comments, subreddit, thread_id))
            
            arquivos_processados += 1

    # Escreve no arquivo final em UTF-8
    if all_texts_to_write:
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.writelines(all_texts_to_write)
        
        print(f"Arquivo gerado: {output_filepath}")
        print(f"Total de arquivos JSON processados: {arquivos_processados}")
        print(f"Total de segmentos de texto: {len(all_texts_to_write)}")
    else:
        print("Nenhum texto válido foi encontrado para processamento.")

# ==========================================
# EXECUÇÃO DO SCRIPT
# ==========================================

def main():
    # Diretório onde estão os arquivos JSON
    pasta_jsons = './jsons'
    # Nome do arquivo final
    arquivo_saida = 'corpus_iramuteq.txt'
    
    process_directory(pasta_jsons, arquivo_saida)

if __name__ == "__main__":
    main()
