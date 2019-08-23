const ExtractTextPlugin = require("extract-text-webpack-plugin");
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


  module: {
    rules: [
      { 
        test: /\.js$/, 
        exclude: /node_modules/,
        loader: "babel-loader"
      },
      {
        test: /\.scss$/,
        use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: ["css-loader","sass-loader"]
        })
      },
    ]
  },

  plugins: [
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: './templates/home/index.html',
    }),
    new ExtractTextPlugin("./css/styles.css"),
  ],
}