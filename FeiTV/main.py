import cadastro
import videos

def main():

    logado = False

    while True:

        print("\n========== FeiTV ==========")

        print("\n1 - Cadastro")
        print("2 - Login")

        print("\n3 - Buscar vídeos")
        print("4 - Listar vídeos")
        print("5 - Curtir")
        print("6 - Descurtir")

        print("\n7 - Criar playlist")
        print("11 - Editar vídeos da playlist")
        print("12 - Excluir playlist")
        print("9 - Adicionar vídeos na playlist")
        print("10 - Remover vídeos da playlist")
        print("8 - Verificar playlist")

        print("\n13 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastro.cadastrar()

        elif opcao == "2":
            if cadastro.login():
                logado = True

        elif not logado:
            print("Faça login primeiro!")

        elif opcao == "3":
            videos.buscar_video()

        elif opcao == "4":
            videos.listar_videos()

        elif opcao == "5":
            videos.curtir_video()

        elif opcao == "6":
            videos.descurtir_video()

        elif opcao == "7":
            videos.criar_playlist()

        elif opcao == "8":
            videos.editar_playlist()

        elif opcao == "9":
            videos.excluir_playlist()

        elif opcao == "10":
            videos.adicionar_video_playlist()

        elif opcao == "11":
            videos.remover_video_playlist()

        elif opcao == "12":
            videos.verificar_playlist()

        elif opcao == "13":
            print("FeiTV encerrado.")
            break

        else:
            print("Opção não encontrada!")

main()