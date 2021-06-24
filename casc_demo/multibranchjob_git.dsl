multibranchPipelineJob('demo/multibranch_git_casc') {
    branchSources {
        git {
            id('12121212') // IMPORTANT: use a constant and unique identifier
            remote('https://github.com/JacksonCHEN63/Django.git')
            credentialsId('github-ci')
            includes('*')
        }
    }
    factory {
      workflowBranchProjectFactory {
        scriptPath('Jenkinsfile')
      }
    }
}
