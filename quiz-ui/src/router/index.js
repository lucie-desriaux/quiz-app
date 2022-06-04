import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import NewQuizPage from '@/views/NewQuizPage.vue'
import QuestionsManager from '@/views/QuestionsManager.vue'
import ResultPage from '@/views/ResultPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: '/start-new-quiz-page',
      name: 'NewQuizPage',
      component: NewQuizPage
    },
    {
      path: '/questions',
      name: 'QuestionsManager',
      component: QuestionsManager
    },
    {
      path: '/results',
      name: 'ResultPage',
      component: ResultPage
    }
  ]
})

export default router
