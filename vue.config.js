const path = require('path');

const resolve = dir => path.join(__dirname, dir);

module.exports = {
  // 基本路径
  publicPath: '/',
  // 生产环境是否生成 sourceMap 文件
  productionSourceMap: false,
  // 服务器端口号
  devServer: {
    port: 80
  },
  chainWebpack: config => {
    config.resolve.alias
      .set('@$', resolve('src'))
      .set('components', resolve('components'))
      .set('assets', resolve('assets'));
  }
};