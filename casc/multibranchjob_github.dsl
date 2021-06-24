multibranchPipelineJob('multibranch_github') {
    branchSources {
        github {
            id('23232323') // IMPORTANT: use a constant and unique identifier
            scanCredentialsId('github-ci')
            repoOwner('JacksonCHEN63')
            repository('Django.git')
            scanCredentialsId('2c3b6aca-62b2-49e5-946f-1b7fdefcc764')
        }
    }
}
