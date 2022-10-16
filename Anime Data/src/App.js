import React,{useState,useEffect,useContext} from "react";
import juju from "./jujutsuKaisen.jpeg";
var view=false;

const url= "https://anime-facts-rest-api.herokuapp.com/api/v1";
const url_bg= "https://api.catboys.com/img";



// document.querySelector("body").style.background=`url(${}}) no-repeat center center / cover`

const AnimeContext = React.createContext();
const App= ()=>{
  const [data,setData]=useState({});
  const [animeName,setAnimeName]=useState("");
  const [animeData,setAnimeData]=useState({});
  const [animeBg,setAnimeBg]=useState('');
  const [bgImg,setBgImg]=useState('');
  const [viewAnime,setViewAnime]=useState(false);
  const [viewAnimeUrl,setViewAnimeUrl]=useState("");

  useEffect(()=>{
    document.querySelector("body").style.background=`linear-gradient(45deg,rgba(102, 232, 255, 0.701),rgba(255, 125, 229, 0.700)),url(${bgImg}) no-repeat center center /cover`;
    document.querySelector("body").style.backgroundAttachment="fixed";
  },[bgImg])
  
  const handleclick=(animeName)=>{
    setAnimeBg("");
    setViewAnime(true);
    setAnimeName(animeName);
    setViewAnimeUrl(`https://anime-facts-rest-api.herokuapp.com/api/v1/${animeName}`);
    document.querySelector(".loadPage").style.display="none";
    window.scrollTo(0,0);
    // document.querySelector("body").style.background=`linear-gradient(45deg,rgba(102, 232, 255, 0.701),rgba(255, 125, 229, 0.700)),url(${animeBg}) no-repeat center center /cover`;
  }

  const handleBack =()=>{
    setViewAnime(false);
    document.querySelector(".loadPage").style.display="block";
    window.scrollTo(0,0);
    document.querySelector("body").style.background=`linear-gradient(45deg,rgba(102, 232, 255, 0.701),rgba(255, 125, 229, 0.700)),url(${bgImg}) no-repeat center center /cover`;
    document.querySelector("body").style.backgroundAttachment="fixed";
  }

  useEffect(()=>{
    fetch(url).then((res)=>res.json()).then((res_data)=>{
      setData(res_data);
      console.log(res_data);
      console.log(data);
    })
  },[url]);
  useEffect(()=>{
    fetch(url_bg).then((res)=>res.json()).then((bg_data)=>{
      const bg_url=bg_data.url;
      // console.log(bg_data);
      setBgImg(bg_url);
      console.log(bgImg);
    })
  },[url_bg]);

  useEffect(()=>{
    fetch(viewAnimeUrl).then((res)=>res.json()).then((anime_data)=>{
      setAnimeData(anime_data);
      setAnimeBg(anime_data.img);
      if (anime_data.img != "https://m.media-amazon.com/images/M/MV5BNzQyYzU3Y2MtOWY2Yy00ZGM2LTg3ZTUtMDJkZTJiMmEzMjYxXkEyXkFqcGdeQXVyMTI2NTY3NDg5._V1_.jpg"){
        document.querySelector("body").style.background=`linear-gradient(45deg,rgba(102, 232, 255, 0.701),rgba(255, 125, 229, 0.700)),url(${anime_data.img}) no-repeat center center /cover`;
      }else{
        document.querySelector("body").style.background=`linear-gradient(45deg,rgba(102, 232, 255, 0.701),rgba(255, 125, 229, 0.700)),url(${juju}) no-repeat center center /cover`
      }
      document.querySelector("body").style.backgroundAttachment="fixed";
      
      // var hei = document.querySelector(".fact>h3").clientHeight;
      // document.querySelector(".fact>span").style.height=hei;
    })
  },[viewAnimeUrl]);



  if(data.success){
    return (
      <AnimeContext.Provider value={{animeData,animeName,handleBack}}>
      <div className="loadPage">
        <h1 className="load">Anime Facts</h1>
          <div className="cardWrapper">
          {
              data.data.map((single_data)=>{
                return (
                  <div className="card" key={single_data.anime_id} onClick={()=>{
                    handleclick(single_data.anime_name);
                  }}>
                    {single_data.anime_img=="https://m.media-amazon.com/images/M/MV5BNzQyYzU3Y2MtOWY2Yy00ZGM2LTg3ZTUtMDJkZTJiMmEzMjYxXkEyXkFqcGdeQXVyMTI2NTY3NDg5._V1_.jpg" ? <img src={juju} alt={single_data.anime_id} /> : <img src={single_data.anime_img} alt={single_data.anime_id} />}
                    <h3>{single_data.anime_name}</h3>
                  </div>
                )
              })
            }
          </div>
        </div>
        {viewAnime && <Anime/>}
      </AnimeContext.Provider>
    )
  }
}

const Anime=()=>{
  const {animeData,animeName,handleBack}=useContext(AnimeContext);
  console.log(animeData);

  
  if(animeData.success){

    return(
      <div className="animePage">
        <h1>{animeName}</h1>
        <div className="back" onClick={handleBack}>Back</div>
        <div className="facts">
          {
            animeData.data.map((singleFact)=>{
              return(
                <div className="fact" key={singleFact.fact_id}>
                  <span>{singleFact.fact_id}</span>
                  <h3>{singleFact.fact}</h3>
                </div>
                
              )
            })
          }
        </div>
      </div>
    )
  }
}

export  {App,view};
