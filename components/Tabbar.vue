<template>
    <van-tabbar route>
        <van-tabbar-item replace to='/' icon="home-o">首页</van-tabbar-item>
        <van-tabbar-item replace to='/discover' icon="search">发现</van-tabbar-item>
        <van-tabbar-item replace to='/community' icon="friends-o">社区</van-tabbar-item>
        <van-tabbar-item replace to='/center' icon="setting-o">我的</van-tabbar-item>
    </van-tabbar>
</template>

<script>
export default {
    data() {
        return {
            active: 0
        }
    }
}
</script>

<style>

</style>