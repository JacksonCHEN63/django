multibranchPipelineJob('multibranch_github') {
    branchSources {
        github {
            id('23232323') // IMPORTANT: use a constant and unique identifier
            scanCredentialsId('github-ci')
            repoOwner('JacksonCHEN63')
            repository('Django.git')
            scanCredentialsId(eaceacf9-c522-4e5f-914d-074a7cbfa6fb)
        }
    }
}
