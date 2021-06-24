multibranchPipelineJob('demo/multibranch_github_casc') {
    branchSources {
        github {
            id('23232323') // IMPORTANT: use a constant and unique identifier
            scanCredentialsId('github-ci')
            repoOwner('JacksonCHEN63')
            repository('Django.git')
            scanCredentialsId('39458efa-107e-454b-a457-f3cb97014354')
        }
    }
}
