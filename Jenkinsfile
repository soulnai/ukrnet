pipeline {
  agent {
    node {
      label 'agent'
    }
    
  }
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