import { create } from 'zustand'

const useReviewStore = create((set) => ({
    // State
    reviews: [],
    currentAnalysis: null,
    isLoading: false,
    error: null,
    pagination: {
        page: 1,
        limit: 10,
        total: 0,
        totalPages: 0,
    },

    // Actions
    setReviews: (reviews) => set({ reviews }),

    setCurrentAnalysis: (analysis) => set({ currentAnalysis: analysis }),

    setLoading: (loading) => set({ isLoading: loading }),

    setError: (error) => set({ error }),

    setPagination: (pagination) => set({ pagination }),

    clearError: () => set({ error: null }),

    clearCurrentAnalysis: () => set({ currentAnalysis: null }),

    // Add new review to the list
    addReview: (review) => set((state) => ({
        reviews: [review, ...state.reviews],
        pagination: {
            ...state.pagination,
            total: state.pagination.total + 1,
        },
    })),
}))

export default useReviewStore
