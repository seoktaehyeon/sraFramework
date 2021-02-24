pipeline {
  agent any
  environment {
    DOCKER_REGISTRY='registry.cn-hangzhou.aliyuncs.com'
  }
  parameters {
    string name: 'GIT_HTTP_URL', trim: true, defaultValue: 'https://github.com/seoktaehyeon/sraFramework.git'
    string name: 'GIT_BRANCH_NAME', trim: true, defaultValue: 'develop'
    string name: 'GIT_CRED', trim: true, defaultValue: 'sraf-devops'
    string name: 'RF_CONFIG', trim: true, defaultValue: 'template.yaml'
    string name: 'RF_TAG', trim: true, defaultValue: 'Demo'
  }
  stages {
    stage('Git Clone') {
      steps {
        deleteDir()
        checkout([
          $class: 'GitSCM',
          branches: [[name: "$GIT_BRANCH_NAME"]],
          doGenerateSubmoduleConfigurations: false,
          extensions: [],
          submoduleCfg: [],
          userRemoteConfigs: [[
            credentialsId: "$GIT_CRED",
            url: "$GIT_HTTP_URL"
          ]]
        ])
      }
    }
    stage('Execute Test Case') {
      steps {
        withDockerContainer(
          image: "${DOCKER_REGISTRY}/bxwill/robotframework:py-chrome-allure",
          args: '--shm-size=1g'
        ) {
          sh """
          ./sraf-cmd --report jenkins-allure --config config/${RF_CONFIG} --tag ${RF_TAG}
          """
        }
      }
      post {
        always {
          allure includeProperties: false, results: [[path: 'output/allure-results']]
        }
      }
    }
  }
}