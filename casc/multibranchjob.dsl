multibranchPipelineJob('multibranch_git') {
    branchSources {
        git {
            id('12121212') // IMPORTANT: use a constant and unique identifier
            remote('https://github.com/JacksonCHEN63/Django.git')
            credentialsId('github-ci')
            includes('JENKINS-*')
        }
    }
    factory {
      workflowBranchProjectFactory {
        scriptPath('Jenkinsfile')
      }
    }
}
