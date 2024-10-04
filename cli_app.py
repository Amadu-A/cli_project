

import openai
import os



# Установите ваш API-ключ
key = ''
openai.api_key = key


def send_query_to_chatgpt(prompt):
    try:
        # Отправка запроса в API OpenAI
        response = openai.Completion.create(
            engine="gpt-4o-mini",  # Вы можете выбрать другой движок, если требуется
            prompt=prompt,
            max_tokens=150,  # Максимальное количество токенов в ответе
            n=1,  # Количество ответов
            stop=None,  # Остановка генерации
            temperature=0.7,  # Контролирует степень случайности в ответах
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Ошибка: {e}"


def main():
    print("Добро пожаловать в консольное приложение ChatGPT.")
    print("Введите 'exit' для завершения.")

    while True:
        # Получение пользовательского запроса
        user_input = input("\nВведите запрос: ")

        if user_input.lower() == 'exit':
            print("Завершение работы...")
            break

        # Отправляем запрос в ChatGPT
        response = send_query_to_chatgpt(user_input)
        print(f"Ответ ChatGPT: {response}")


if __name__ == "__main__":
    main()