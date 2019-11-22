import speech_recognition as sr#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        #Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)
        try:
            #Passa o audio para o reconhecedor de padroes do speech_recognition
            frase = microfone.recognize_google(audio,language='pt-BR')
            #Após alguns segundos, retorna a frase falada
            print("Você disse: " + frase)#Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.UnkownValueError:
            print("Não entendi")
        return fraseouvir_microfone()
import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

ouvir_microfone()
