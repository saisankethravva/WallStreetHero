pipeline {

    environment {
         registry = "dockerimagessjsu/file_studio_docker_image"
         registryCredential = 'dockerhub_id_1'
         tag = "wall_street_backend"
         dockerImage = ''
    }

    agent any

    stages {
        stage('SCM Checkout our git') {
            steps {
                echo 'Checking out SCM repo'
                sh '''#!/bin/bash
                    pwd
                    ls -al
                    echo "Current User"
                    id
                '''
            }
        }
        stage('build image') {
            steps {
                echo 'Building Docker Image'
                script {
                    dockerImage = docker.build registry +":$tag"
                }
            }
        }
        stage('push image') {
            steps {
                echo 'pushing image to docker hub'
                 script {
                  docker.withRegistry( '', registryCredential ) {
                  dockerImage.push()
                    }
                }
            }
        }
        stage('Cleaning up') {
            steps {
                sh "docker system prune -a --volumes -f"
                cleanWs()
                deleteDir()
            }
        }
    }
}

