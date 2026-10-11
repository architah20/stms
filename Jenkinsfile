
pipeline {
    agent any

    triggers {
        pollSCM('H/1 * * * *')
    }

    environment {
        IMAGE_NAME = 'stms'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && cd app && pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Deploy (local container)') {
            steps {
                sh '''
                    docker stop stms-jenkins-app || true
                    docker rm stms-jenkins-app || true
                    docker run -d --name stms-jenkins-app -p 5002:5000 ${IMAGE_NAME}:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded. App running on port 5002.'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}
