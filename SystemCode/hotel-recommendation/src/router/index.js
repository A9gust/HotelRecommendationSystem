import Vue from "vue";
import Router from "vue-router";
import UserSignup from "@/components/UserSignup.vue";
import IdealVacation from "@/components/IdealVacation.vue";
import UserSelection from "@/components/UserSelection.vue";
import RecommendResult from "@/components/RecommendResult.vue";
import UserRate from "@/components/UserRate.vue";
import BookingPage from "@/components/BookingPage.vue";
import HomePage from "@/components/HomePage.vue";
import SystemRate from "@/components/SystemRate.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/user-signup",
      name: "UserSignup",
      component: UserSignup,
    },
    {
      path: "/ideal-vacation",
      name: "IdealVacation",
      component: IdealVacation,
    },
    {
      path: "/user-selection",
      name: "UserSelection",
      component: UserSelection,
    },
    {
      path: "/user-rate",
      name: "UserRate",
      component: UserRate,
    },
    {
      path: "/recommend-result",
      name: "RecommendResult",
      component: RecommendResult,
    },
    {
      path: "/user-booking",
      name: "BookingPage",
      component: BookingPage,
    },
    {
      path: "/system-rate",
      name: "SystemRate",
      component: SystemRate,
    },
  ],
});
