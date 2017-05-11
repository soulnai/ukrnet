pipeline {
  agent any
  stages {
    stage('script') {
      steps {
        sh 'echo "test"'
      }
    }
    stage('errors') {
      steps {
        catchError()
      }
    }
  }
}