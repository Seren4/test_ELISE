<template>
    <MainComponent/>
</template>

<script>
    import MainComponent from './components/MainComponent.vue'

    export default {
        name: 'app',
        components: {
            MainComponent
        }
    }
</script>

<style>
    * {
        margin: 0;
        padding: 0;
    }
    body {
        width: 1080px;
        height: 1920px;
    }
</style>
