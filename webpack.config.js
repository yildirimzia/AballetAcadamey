const HtmlWebpackPlugin = require('html-webpack-plugin');
const path =require('path');


module.exports = {
  entry: ["@babel/polyfill", "./static/js/index.js"],
  
  output: {
    path: path.resolve(__dirname,'dist'),
    filename: 'js/bundle.js'
  },

  devServer: {
    contentBase: './dist'
  },

  plugins: [
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: './templates/home/index.html'
    })
  ],

  module: {
    rules: [
      { 
        test: /\.js$/, 
        exclude: /node_modules/,
        loader: "babel-loader"
      },
      {
        test: /\.scss$/,
        use: ['style-loader', 'css-loader','sass-loader'],
      },
    ]
  }
}