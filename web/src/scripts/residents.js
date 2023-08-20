export default {
    data() {
        return {
            residents: [
                {id: 0, image: '/images/image1.jpg', title: 'Бар "Куйбышева"', info: 'Танцевальный бар с прекрасной волжской кухней и живыми концертами.', push_path: '/resident-main/resident-one'},
                {id: 1, image: '/images/image2.jpg', title: 'Монобар "Проходная', info: 'Монобар с говорящим названием, который перенесет тебя совершенно в другое место - проходную советского завода.', push_path: '/resident-main/resident-two'},
                {id: 2, image: '/images/image3.jpg', title: 'Ulandy Cafe', info: 'Еда на каждый день, которую удобно взять с собой! Наш гравный принцип - супер фреш.', push_path: '/resident-main/resident-three'},
                {id: 3, image: '/images/image4.jpg', title: 'Бистро "Зозо"', info: 'Современное ретро Битсро с открытой кухней.', push_path: '/resident-main/resident-four'}
            ],
        }
    },
    methods: {
        LoadInfoPage(path) {
            this.$router.push(path)
        }
    }
}