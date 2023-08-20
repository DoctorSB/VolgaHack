export default {
    data() {
        return {
            residents: [
                {id: 0, image1path: '/images/image1.jpg', header: 'Бар "Куйбышева"', information: 'Танцевальный бар с прекрасной волжской кухней и живыми концертами.', info_page_file: '/resident-one'},
                {id: 1, image1path: '/images/image2.jpg', header: 'Монобар "Проходная', information: 'Монобар с говорящим названием, который перенесет тебя совершенно в другое место - проходную советского завода.', info_page_file: '/resident-two'},
                {id: 2, image1path: '/images/image3.jpg', header: 'Ulandy Cafe', information: 'Еда на каждый день, которую удобно взять с собой! Наш гравный принцип - супер фреш.', info_page_file: '/resident-three'},
                {id: 3, image1path: '/images/image4.jpg', header: 'Бистро "Зозо"', information: 'Современное ретро Битсро с открытой кухней.', info_page_file: '/resident-four'}
            ],
        }
    },
    methods: {
        LoadInfoPage(path) {
            this.$router.push(path)
        }
    }
}