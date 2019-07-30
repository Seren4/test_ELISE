<template>
  <div id="main">
    <!-- show the video only if the are no errors-->
    <div v-if="!error">
      <!--video -->
      <video
              id="my-player"
              class="video-js"
              preload="auto"
              data-setup='{}'
              muted="muted"
              @timeupdate="TimeUpdate"
      >
        <source src="https://custom-templates-assets.s3-eu-west-1.amazonaws.com/op-6450/video-airelise.webm" type="video/webm"/>
      </video>

      <!--photo slider -->
      <div class="polaroid" v-if="photos && ShowPhotos"  v-for="number in [currentImg]" :key="number"
           :style="{ backgroundImage: 'url(' + photos[Math.abs(currentImg) % photos.length].content + ')'  }"
           :class="[VideoPlay ? 'play-class' : 'pause-class']"
      >
      </div>

      <!--logo -->
      <div class="logo">
        <img src="https://elise.tech/wp-content/uploads/2017/07/elise-technologies-logo-white-300x147.png" alt="">
      </div>

      <!--banner -->
      <div class="banner">
        <p v-if="banner && ShowBanner"> {{banner}} </p>
      </div>
    </div>

    <!-- display error -->
    <div v-else class="error">
      <h4>{{error}}</h4>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'MainComponent',
    data () {
      return {
        // photo slider index
        currentImg: 0,
        // page content variables
        photos: null,
        banner: '',
        error: null,
        // flag to show/hide photos and banner
        ShowPhotos: false,
        ShowBanner: false,
        // flag to pause/play the CSS photo animation
        VideoPlay: false
      }
    },
    mounted () {
      this.ConfigVideo();
      this.GetContent()
    },
    methods: {
      // server request to get photos and banner
      async GetContent () {
        // reset error to null before each request
        this.error = null;
        try {
          const response = await this.$axios.get('/get_content');
          // check response and response content
          if (response && response.data) {
            if (response.data.photos && response.data.banner) {
              this.photos = response.data.photos;
              this.banner = response.data.banner.content
            } else { this.error = 'Api error, please refresh the page' }
          }
        }
                // handle server error
        catch (e) {
          this.error = 'Api error, please refresh the page'
        }
      },
      // keep track of video current position to show/switch photos
      TimeUpdate () {
        let video = document.getElementById('my-player');
        if (video) {
          // show photos after 1 seconds
          if (video.currentTime >= 1) { this.ShowPhotos = true }
          // switch photo after 5 seconds, only if the video is playing
          if (video.currentTime >= video.duration / 2 && !video.paused) { this.currentImg = 1 }
        }
      },
      // configuration
      ConfigVideo () {
        let self = this;
        let video = document.getElementById('my-player');
        if (video) {
          document.onkeydown = function (e) {
            // play/pause with P button
            if (e['keyCode'] === 80) {
              // show the banner
              self.ShowBanner = true;
              if (video.paused) {
                self.VideoPlay = true;
                video.play()
              } else {
                video.pause();
                self.VideoPlay = false
              }
            }
            // reset player with R button
            if (e['keyCode'] === 82) {
              // make new request
              self.GetContent();
              // hide photos and banner
              self.ShowPhotos = false;
              self.ShowBanner = false;
              // reset player
              video.pause();
              video.currentTime = 0;
              // reset photo slider index
              self.currentImg = 0
            }
          }
        }
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #main{
    display: flex;
  }

  #my-player {
    position: absolute;
    width: 1080px;
    height: 1920px;
  }

  /*photo slider style and animation*/
  .polaroid {
    min-height: 600px;
    border: 18px solid #ffffff;
    border-bottom: 80px solid #ffffff;
    z-index: 10;
    position: relative;
    top: 700px;
    left: 240px;
    min-width: 600px;
    background-size: 220%;
    background-repeat: no-repeat;
    background-position: center 60%;

    -ms-transform: rotate(10deg); /* IE 9 */
    -webkit-transform: rotate(10deg); /* Safari 3-8 */
    transform: rotate(10deg);

    animation: animatedBackground 4.7s linear, fadein 1.5s ;
    animation-iteration-count: 1;

    -webkit-animation: animatedBackground 4.7s linear, fadein 1.5s;
    -webkit-animation-iteration-count:  1;
  }

  @keyframes animatedBackground {
    from { background-position: center 30%; }
    to { background-position: center 60%; }
  }
  @-moz-keyframes animatedBackground { /* Firefox */
    from { background-position: center 30%; }
    to { background-position: center 60%; }
  }
  @-webkit-keyframes animatedBackground { /* Safari and Chrome */
    from { background-position: center 30%; }
    to { background-position: center 60%; }
  }

  .logo {
    display: block;
    z-index: 2;
    position: absolute;
    top: 1500px;
    left: 390px;
    width: 100%;
    max-width: 400px;
  }

  /*banner style and animation*/
  .banner{
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #ffffff;
    z-index: 1;
    position: absolute;
    top: 1840px;
    width: 1080px;
    height: 80px;
  }

  .banner p{
    font-family: Helvetica, serif;
    font-size: 25px;
    -webkit-animation: fadein 1s; /* Safari, Chrome and Opera > 12.1 */
    -moz-animation: fadein 1s; /* Firefox < 16 */
    -o-animation: fadein 1s; /* Opera < 12.1 */
    animation: fadein 1s;
  }
  @keyframes fadein {
    from { opacity:0; }
    to { opacity:1; }
  }
  @-moz-keyframes fadein { /* Firefox */
    from { opacity:0; }
    to { opacity:1; }
  }
  @-webkit-keyframes fadein { /* Safari and Chrome */
    from { opacity:0; }
    to { opacity:1; }
  }

  /*play/pause photo animation classes*/
  .play-class{
    animation-play-state: running;
  }
  .pause-class{
    animation-play-state: paused;
  }

  .error{
    display: block;
    position: absolute;
    top: 50%;
    left: 50%;
  }
</style>
