pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/adiaharony/Magic-Decision-Maker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('magic-decision-app')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop any previous container with the same name
                    sh 'docker rm -f magic-app || true'

                    // Run a new container
                    sh 'docker run -d -p 5000:5000 --name magic-app magic-decision-app'
                }
            }
        }
    }
}
