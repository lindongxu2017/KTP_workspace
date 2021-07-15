export default {
    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: 'Nuxt-mobile-app',
        htmlAttrs: {
            lang: 'en'
        },
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no' },
            { hid: 'description', name: 'description', content: '' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
        ],
        script: [
            { src: 'http://g.tbcdn.cn/mtb/lib-flexible/0.3.2/??flexible_css.js,flexible.js' }
        ]
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
        'vant/lib/index.css'
    ],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [
        '@/plugins/vant',
        // {
        //     src: '@/plugins/lib-flexible',
        //     ssr: false
        // }
    ],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        // https://go.nuxtjs.dev/axios
        '@nuxtjs/axios',
    ],

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {},

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {
        postcss: {
            plugins: {
                'postcss-px2rem-exclude': {
                    remUnit: 37.5, // 设计图为750 * height
                    remPrecision: 2, // rem的小数点后位数
                    // exclude: /node_modules|folder_name/i //取消vant组件css转成rem 忽略node_modules目录下的文件
                }
            }
        },
    }
}