pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'magic-decision-maker'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/AdiAharony/Magic-Decision-Maker.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build(env.DOCKER_IMAGE)
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    dockerImage.run('-p 5000:5000')
                }
            }
        }
    }
}
