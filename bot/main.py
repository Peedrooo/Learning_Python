from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from resources import (
    contatos, mensagem, midia, aguardar_chrome, aguardar_busca_contato,
    aguardar_mensagem, aguardar_midia, tempo_espera_geral
)
import time
import os


def chrome():
    try:
        print('Abrindo o Chrome')
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://web.whatsapp.com/')
        time.sleep(aguardar_chrome)
    except Exception as error:
        print("Erro ao abrir o chrome\n", error)
        exit()


def buscar_contato(contato):
    try:
        print('Buscando contato/grupo: ', contato)
        campo_pesquisa = driver.find_element(
            By.XPATH, '//p[contains(@class,"selectable-text copyable-text")]'
            )
        time.sleep(aguardar_busca_contato)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        campo_pesquisa.send_keys(Keys.ENTER)
    except Exception:
        print("Contato/Grupo não encontrado")
        novamente = input('Tentar novamente? (s/n): ')
        if novamente in 'Ss':
            buscar_contato(contato)
        else:
            exit()


def enviar_mensagem(mensagem):
    try:
        print('Enviando mensagem')
        campo_mensagem = driver.find_elements(
            By.XPATH, '//p[contains(@class,"selectable-text copyable-text")]'
            )
        campo_mensagem[1].click()
        time.sleep(aguardar_mensagem)
        campo_mensagem[1].send_keys(mensagem)
        campo_mensagem[1].send_keys(Keys.ENTER)
    except Exception as error:
        print("Erro ao enviar mensagem", error)
        exit()


def enviar_midia(midia):
    try:
        midia = os.getcwd() + midia
        driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
        attach = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        attach.send_keys(midia)
        time.sleep(aguardar_midia)
        send = driver.find_element(By.CSS_SELECTOR, "span[data-icon='send']")
        send.click()
    except Exception as error:
        print("Erro ao enviar midia", error)
        exit()


if __name__ == '__main__':
    chrome()
    for contato in contatos:
        buscar_contato(contato)
        enviar_mensagem(mensagem)
        enviar_midia(midia)
        time.sleep(tempo_espera_geral)
    print('Fim do processo')
