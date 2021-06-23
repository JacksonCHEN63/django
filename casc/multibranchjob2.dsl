multibranchPipelineJob('example2') {
    branchSources {
        github {
            id('23232323') // IMPORTANT: use a constant and unique identifier
            scanCredentialsId('github-ci')
            repoOwner('JacksonCHEN63')
            repository('Django')
        }
    }
}
