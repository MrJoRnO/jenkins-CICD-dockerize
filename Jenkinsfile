pipeline {
    agent any
    
    environment {
        DOCKER_HUB_USER = 'noamjorno'
        IMAGE_NAME = 'myapp'
        IMAGE_TAG = "${env.BUILD_ID}"
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
    }
    
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }
        
        stage('Tag and Push to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                        sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                        sh "docker tag ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                        sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                    }
                }
            }
        }
        
//         stage('Deployment with Ansible') {
//             steps {
//                 script {
//                     sh "ansible-playbook deploy-playbook.yml -e 'image_tag=${IMAGE_TAG} image_name=${DOCKER_HUB_USER}/${IMAGE_NAME}'"
//                 }
//             }
//         }
//     }
    
        post {
            always {
                sh "docker logout"
            }
        }
    }
}