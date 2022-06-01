pipeline {
    agent any

    stages{
        stage('PreBuild') {
            steps {
                git branch: 'main', url: 'https://github.com/qa-lenvendo/OtusProject.git'
                sh 'mkdir -p allure-results'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t project_tests . < Dockerfile'
            }
        }
        stage('Tests') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh """docker run --name project_tests --network selenoid --mode=remote --stand=${STAND} --browser_name=${BROWSER} --hub=${EXECUTOR_HUB} --hub_port=${EXECUTOR_PORT} -n ${STREAM_NUM}"""
                }
            }
        }
        stage('Copy Artefact') {
            steps {
                sh 'docker cp project_tests:/app/allure-results .'
            }
        }
        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
    post {
        always {
            sh 'docker rm project_tests'
        }
    }
}