pipeline {
    agent {
        docker {
            image 'docker:19.03.12-dind'  // Docker image with DinD support
            args '--privileged'  // Allow Docker-in-Docker (DinD) functionality
        }
    }
    environment {
        DOCKER_IMAGE = 'my-app-image'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository to get the code and Jenkinsfile
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image from the Dockerfile in the repo
                    sh 'docker build -t $DOCKER_IMAGE .'  // Builds the Docker image
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container 
                    sh 'docker run -d $DOCKER_IMAGE'  // Run the container in detached mode
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    // Stop the container and remove it 
                    sh 'docker ps -q --filter "ancestor=$DOCKER_IMAGE" | xargs docker stop | xargs docker rm'
                }
            }
        }
    }
    post {
        always {
            // Clean up any resources after the build 
            sh 'docker rmi $DOCKER_IMAGE || true'  // Remove the Docker image after use
        }
    }
}
