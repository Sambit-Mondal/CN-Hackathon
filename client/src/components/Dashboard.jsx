

const Dashboard = () => {
    return (
        <div className="w-[70%] h-[80%] border-2 border-mlsa-sky-blue rounded-md px-5 py-2 overflow-hidden overflow-y-auto">
            <div className='sticky top-0 w-full bg-mlsa-bg pb-1'>
                <div className="font-bold flex items-center justify-between py-3">
                    <div className="text-white text-lg">Dashboard</div>
                </div>
                <hr className="border-none h-1 bg-mlsa-sky-blue mb-4" />
                <div className="overflow-hidden overflow-y-auto w-full">
                </div>
            </div>
        </div>
    )
}

export default Dashboard