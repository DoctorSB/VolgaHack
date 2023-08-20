export default {
    data() {
        return {
            clusters: [
                {id: 0, image: '/images/image1.jpg', title: 'Бар "Куйбышева"', info: 'Танцевальный бар с прекрасной волжской кухней и живыми концертами.', resident_path: '/resident-main'},
            ],
        }
    },
    methods: {
        LoadInfoPage(path) {
            this.$router.push(path)
        }
    }
}