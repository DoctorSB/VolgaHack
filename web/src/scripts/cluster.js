export default {
    data() {
        return {
            clusters: [
                {id: 0, image: '/images/artfactory.jpg', plot_image: '/images/square_word_art_fabric.png', title: 'Станкозавод', info: 'Центр труда и отдыха Станкозавод — третье место, где можно работать, общаться, создавать свою среду, строить планы и воплощать мечты. Это рабочее и социальное пространство новаторов, лидеров мнений, творцов и созидателей.', resident_path: '/resident-main'},
                {id: 1, image: '/images/house77.jpg', plot_image: '/images/square_word_art_fabric.png', title: 'Дом 77', info: 'Творческий кластер наполнен ремесленными и художествеными мастерскими, шоу-румами, авторскими сэкондами, репетиционными и танцевальными студиями, кофейней, летней площадкой, баром «Вечно молодой» и центром современной культуры «Нулевая комната».', resident_path: '/resident-main'},
            ],
        }
    },
    methods: {
        LoadInfoPage(path) {
            this.$router.push(path)
        }
    }
}