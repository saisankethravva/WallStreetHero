import FeaturedInfo from "../../components/featuredInfo/FeaturedInfo";
import Chart from "../../components/charts/Chart";
import "./home.css";
import { userData } from "../../dummyData";
import Gainers from "../../components/gainers/gainers";
import Losers from "../../components/losers/losers";
import TrendingTickers from "../../components/trendingTickers/trendingTickers";
import News from "../../components/news/news";
import SectorPerformance from "../../components/sectorPerformance/sectorPerformance";
import RedditMentions from '../../components/redditMentions/redditMentions';
import Topbar from '../../components/topbar/topbar';
import MarketHours from "../../components/marketHours/marketHours";


export default function Home() {
  return (
    <div className="home">
      <div>
         <Topbar />
     </div>
      <MarketHours />
      <News />
      {/* <FeaturedInfo /> */}
      {/* <Chart
        data={userData}
        title="User Analytics"
        grid
        dataKey="Active User"
      /> */}
      <div className="topNTables">
        <Gainers />
        <Losers />
        <SectorPerformance />
      </div>
      <div className="topNTables">
        <RedditMentions />
        <TrendingTickers />
      </div>
    </div>
  );
}
