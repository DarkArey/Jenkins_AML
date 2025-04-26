pipeline {
    // Процесс сборки может быть выполнен на любом доступном агенте Jenkins
    agent any

    stages {
        // Клонируем репозиторий Git Jenkins_AML, устанавливаем ветку main
        stage('Checkout') {
            steps {
                git url:'https://github.com/DarkArey/Jenkins_AML.git', branch: 'main'
            }
        }
        // Установка всех зависимостей Python-проекта
        stage('Install') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        // Тестирование проекта
        stage('Test') {
            steps {
                bat 'python -m pytest'
            }
        }
    }
}