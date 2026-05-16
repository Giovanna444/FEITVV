videos_lista = [

    {"Titulo": "Aula de CSS",
     "Genero": "Educativo",
     "Duracao": 15,
     "Diretor": "Cristiane",
     "Curtidas": 0},

    {"Titulo": "Aula de HTML",
     "Genero": "Curso",
     "Duracao": 16,
     "Diretor": "Giovanna",
     "Curtidas": 0},

    {"Titulo": "Aula de Python",
     "Genero": "Programação",
     "Duracao": 17,
     "Diretor": "Murilo",
     "Curtidas": 0}
]

# PLAYLIST

playlist = {
"Favoritos": []
}

# LISTAR VÍDEOS

def listar_videos():

    for v in videos_lista:

        print("\n--- VÍDEO ---")
        print("Título:", v["Titulo"])
        print("Gênero:", v["Genero"])
        print("Duração:", v["Duracao"])
        print("Diretor:", v["Diretor"])
        print("Curtidas:", v["Curtidas"])

# BUSCAR VÍDEO

def buscar_video():

    tipo = input("Buscar por (Titulo, Genero, Diretor, Duracao)?: ").lower().strip()
    valor = input("Digite o valor da busca: ")

    resultados = []

    for v in videos_lista:

        if tipo == "duracao":

            if v["Duracao"] == int(valor):
                resultados.append(v)

        else:

            mapa = {
                "titulo": "Titulo",
                "genero": "Genero",
                "diretor": "Diretor"
            }

            if tipo in mapa:

                if str(v[mapa[tipo]]).lower() == valor.lower():
                    resultados.append(v)

    print("\n===== RESULTADO: =====")

    if len(resultados) == 0:

        print("Esse vídeo não existe!")

    else:

        for v in resultados:

            print("\nTítulo:", v["Titulo"])
            print("Gênero:", v["Genero"])
            print("Duração:", v["Duracao"])
            print("Diretor:", v["Diretor"])
            print("Curtidas:", v["Curtidas"])

# CURTIR

def curtir_video():

    titulo = input("Titulo do vídeo: ")

    for v in videos_lista:

        if v["Titulo"].lower() == titulo.lower():

            v["Curtidas"] += 1

            print("Vídeo curtido!")
            print("Total de curtidas:", v["Curtidas"])
            return

    print("Vídeo não encontrado!")

# DESCURTIR

def descurtir_video():

    titulo = input("Titulo do vídeo: ")

    for v in videos_lista:

        if v["Titulo"].lower() == titulo.lower():

            if v["Curtidas"] > 0:
                v["Curtidas"] -= 1

            print("Descurtido!")
            print("Total de curtidas:", v["Curtidas"])
            return

    print("Vídeo não encontrado!")

# CRIAR PLAYLIST

def criar_playlist():

    nome = input("Nome da playlist: ")

    if nome in playlist:

        print("Essa playlist já existe!")
        return

    playlist[nome] = []

    print("Playlist criada!")

# VER PLAYLIST

def verificar_playlist():

    nome = input("Nome da playlist: ")

    if nome not in playlist:

        print("Não existe!")
        return

    print("\n===== PLAYLIST =====")

    if len(playlist[nome]) == 0:

        print("Playlist vazia!")
        return

    for v in playlist[nome]:

        print("\nTítulo:", v["Titulo"])
        print("Gênero:", v["Genero"])
        print("Duração:", v["Duracao"])
        print("Diretor:", v["Diretor"])
        print("Curtidas:", v["Curtidas"])

# EXCLUIR PLAYLIST

def excluir_playlist():

    nome = input("Nome da playlist: ")

    if nome not in playlist:

        print("Essa playlist não existe!")
        return

    del playlist[nome]

    print("Playlist excluída!")

# ADICIONAR VÍDEO NA PLAYLIST

def adicionar_video_playlist():

    nome_playlist = input("Nome da playlist: ")
    titulo_video = input("Título do vídeo: ")

    if nome_playlist not in playlist:

        print("Playlist não encontrada!")
        return

    for v in videos_lista:

        if v["Titulo"].lower() == titulo_video.lower():

            playlist[nome_playlist].append(v)

            print("Vídeo adicionado!")
            return

    print("Vídeo não encontrado!")

# REMOVER VÍDEO DA PLAYLIST

def remover_video_playlist():

    nome_playlist = input("Nome da playlist: ")
    titulo_video = input("Título do vídeo: ")

    if nome_playlist not in playlist:

        print("Playlist não encontrada!")
        return

    for v in playlist[nome_playlist]:

        if v["Titulo"].lower() == titulo_video.lower():

            playlist[nome_playlist].remove(v)

            print("Vídeo removido!")
            return

    print("Vídeo não encontrado!")

# EDITAR VÍDEO NA PLAYLIST

def editar_playlist():

    nome_playlist = input("Nome da playlist: ")
    antigo = input("Vídeo atual: ")
    novo = input("Novo vídeo: ")

    if nome_playlist not in playlist:

        print("Playlist não encontrada!")
        return

    video_novo = None

    for v in videos_lista:

        if v["Titulo"].lower() == novo.lower():

            video_novo = v
            break

    if video_novo is None:

        print("Este vídeo não existe!")
        return

    for i in range(len(playlist[nome_playlist])):

        if playlist[nome_playlist][i]["Titulo"].lower() == antigo.lower():

            playlist[nome_playlist][i] = video_novo

            print("Playlist atualizada!")
            return
