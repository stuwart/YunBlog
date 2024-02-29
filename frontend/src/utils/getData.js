

import axios from "axios"
const fetchArticles = async (url) => {
    try {
      const response = await axios.get(url);
      articles.value = await response.data.results;
      console.log(articles);
    } catch (error) {
      console.error("There is an error:", error);
    }
  };


  export default fetchArticles;