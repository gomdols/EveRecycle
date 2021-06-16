module.exports = {
    module: {
      rules: [
        {
            test: /\.js$/,
            exclude: /node_modules/,
            use: {
                loader: "babel-loader"
            }
        },
        {
            test: /\.css$/i,
            use: ["style-loader", "css-loader"],
        },
        {
            test: /\.(jpe?g|png|gif|svg)$/i,
            use: [
              'url-loader?limit=10000',
              'img-loader'
            ]
        }
      ]
    }
  };